This is a **renamed version** of `chargebee-python`, which can be useful
to work with both version 1 and version 2 of the chargebee API.

If you just want to use one version of the official chargebee client,
please refer to the original project and documentation.

Setup
=====

Let me stress this out: you need this only if you need to work with both
v1 and v2 versions of the chargebee API; if you don't, please refer to
the original project.

In your `requirements.txt`:
```
chargebee==1.6.3
https://github.com/armisael/chargebee-python/tarball/e414c551b217a077f7d17b3d43a74c0d0752922c  # v2.6.2
```

Then simply configure both versions with the same parameters:
```
import chargebee
import chargebee_v2

chargebee.configure(CHARGEBEE_API_KEY, CHARGEBEE_SITE_NAME)
chargebee_v2.configure(CHARGEBEE_API_KEY, CHARGEBEE_SITE_NAME)
```

And you're good to go:
```
    # retrieve the coupon code with API v2, which returns also the coupon status
    res_v2 = chargebee_v2.CouponCode.retrieve(coupon_code)

    if res_v2.coupon_code.status == 'not_redeemed':
        # retrieve the coupon with API v1, for backward compatibility of our project code
        res_v1 = chargebee.Coupon.retrieve(res_v2.coupon_code.coupon_id)
```

How to update
=============

This repo will most likely never be updated, but if you need to,
simply:
- clone this project
- merge the latest version of the official repo
- keep all their changes
- make sure all the files are in a folder named `chargebee_v2`
- make sure the `setup.py` imports from there, and names the project
  `chargebee_v2`
- replace all the occurrences of `from chargebee.` with `from chargebee_v2.`;
  the easiest way to do it is to open PyCharm and perform a "Replace in path".
- also check that `MANIFEST.in` points to the new folder that contains `ca-certs.crt`